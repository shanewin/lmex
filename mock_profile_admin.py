import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import PersonalProfile, NFT, Wallet

# Get Admin User
try:
    user = User.objects.get(username='admin')
except User.DoesNotExist:
    print("Admin user not found! Please create it first.")
    exit(1)

print(f"Updating data for: {user.username}")

# 1. Update Personal Profile
profile, created = PersonalProfile.objects.get_or_create(user=user)
profile.full_name = "Shane Winter" # Using user's likely name based on file paths/context or just a generic one. Let's use "Admin Student" as per plan or maybe "Shane Winter" since he's the user. 
# The prompt didn't specify the exact name, but "Admin Student" was in my plan. I'll stick to a generic "Student Admin" or the user's name if I want to be nice. 
# Prompt said "dummy full names". I'll use "Student Admin" or actually "Shane Winter" is better since he is the user. 
# Let's stick to "Student Admin" to be safe/generic as per plan. 
profile.full_name = "Student Admin" 
profile.save()
print(f"  - Profile Name: {profile.full_name}")

# 2. Update NFT Info
nft, created = NFT.objects.get_or_create(user=user)
nft.name = "Student Genesis ID #001"
nft.description = "Verified Identity for LMeX Pilot Program. Validated by Biometric Scan and Community Approval."
nft.image_ipfs_uri = "QmXyZ1234567890abcdef1234567890abcdef123456" # Dummy Hash
nft.contract_address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
nft.token_id = "101"

# Assign an image (reuse one of the generated ones)
# We know the files exist in media/nft_images/ from previous step
# Let's pick avatar 2 (Cool headphones)
nft.image.name = "nft_images/student_avatar_2_1765207398272.png"
nft.save()
print(f"  - NFT Name: {nft.name}")
print(f"  - NFT Hash: {nft.image_ipfs_uri}")
print(f"  - NFT Image: {nft.image.name}")

# 3. Update Wallet Info
wallet, created = Wallet.objects.get_or_create(user=user)
wallet.wallet_address = "0xABC1234567890abcdef1234567890abcdef123456"
wallet.save()
print(f"  - Wallet: {wallet.wallet_address}")

print("Done! Admin profile updated.")
