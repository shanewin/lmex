import os
import secrets
from dotenv import load_dotenv

# Load the .env file from the 'battle-website' directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

try:
    from thirdweb import ThirdwebSDK
    from thirdweb.types import SDKOptions, GasSettings, GasSpeed
    from eth_account import Account
    from thirdweb.types.nft import NFTMetadataInput
    from web3 import Web3
except ImportError:
    ThirdwebSDK = None
    SDKOptions = None
    GasSettings = None
    GasSpeed = None
    Account = None
    NFTMetadataInput = None
    Web3 = None

# Access the environment variables
THIRDWEB_API_KEY = os.getenv('THIRDWEB_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
CONTRACT_ADDRESS = os.getenv('NFT_CONTRACT_ADDRESS', "0xACC9F82e68611630B718D646951538C81b7a57ab")
NFT_IMAGE_PATH = os.getenv('NFT_IMAGE_PATH', "/path/to/default/image.png")

def mint_nft_script():
    if not (ThirdwebSDK and Account):
        return

    # Generating a random hexadecimal string and storing it in priv variable
    priv = secrets.token_hex(32)
    # Attaching 0x prefix to our 64 character hexadecimal string stored in priv and storing the new string in variable private_key.
    private_key = "0x" + priv
    # Creating a new account using the private_key and storing it in variable acct
    wallet_account = Account.from_key(private_key)
    # Get the Ethereum wallet address from the Account instance
    wallet_address = wallet_account.address

    # Create the gas settings with your desired values
    gas_settings = GasSettings(max_price_in_gwei=300000000000, speed=GasSpeed.FAST)

    # Create SDK options with the gas settings
    options = SDKOptions(gas_settings=gas_settings)

    # Create a valid signer using your private key
    signer = Account.from_key(PRIVATE_KEY)

    # Create the SDK
    sdk = ThirdwebSDK("goerli", options=SDKOptions(secret_key=THIRDWEB_API_KEY))

    sdk.update_signer(signer)


    contract = sdk.get_contract(CONTRACT_ADDRESS)

    try:
        image_file = open(NFT_IMAGE_PATH, "rb")
    except FileNotFoundError:
        return

    metadata = NFTMetadataInput.from_json({
        "name": "Cool NFT",
        "description": "This is a cool NFT",
        "image": image_file,
    })

    tx = contract.erc721.mint_to(wallet_address, metadata)
    receipt = tx.receipt
    token_id = tx.id
    nft = tx.data()


if __name__ == "__main__":
    mint_nft_script()
