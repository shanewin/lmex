import os
import django
from django.core.files import File
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import PersonalProfile, NFT

# Mock Data
names = [
    "Jordan Tech", "Alex Coder", "Taylor Swift (Not that one)", 
    "Casey Blockchain", "Morgan DeFi", "Riley Token", "Jamie Smart"
]

avatars = [
    "nft_images/student_avatar_1_1765207312531.png",
    "nft_images/student_avatar_2_1765207398272.png",
    "nft_images/student_avatar_3_1765207509038.png"
]

users = User.objects.exclude(is_superuser=True)

for i, user in enumerate(users):
    print(f"Updating {user.username}...")
    
    # Update Profile
    profile, created = PersonalProfile.objects.get_or_create(user=user)
    profile.full_name = names[i % len(names)]
    profile.save()
    print(f"  - Set name to {profile.full_name}")

    # Update NFT
    nft, created = NFT.objects.get_or_create(user=user)
    nft.image_ipfs_uri = ""  # Clear IPFS to force local fallback
    
    # Assign random avatar
    # Note: In a real app we'd open the file and save it to the ImageField, 
    # but since we manually copied files to media/nft_images/, 
    # we can just set the path directly if the file exists.
    # However, Django ImageField stores the path relative to MEDIA_ROOT.
    
    avatar_file = avatars[i % len(avatars)]
    # We copied them to media/nft_images/filename.png
    # The DB expects 'nft_images/filename.png'
    
    # Let's clean the path to be relative to media root
    relative_path = os.path.basename(avatar_file)
    nft.image.name = f"nft_images/{relative_path}"
    nft.save()
    print(f"  - Set image to {nft.image.name}")

print("Done!")
