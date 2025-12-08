import os
import django
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
django.setup()

from django.contrib.auth.models import User
from lms.models import Post, Reply, Unit, UpvoteEvent, Reply
from users.models import Wallet, PersonalProfile, NFT

def seed_data():
    print("Beginning Database Seed...")
    
    # 1. Create Units
    units = ["Unit 1: Budgeting", "Unit 2: Saving", "Unit 3: Investing", "Unit 4: Crypto"]
    for u_name in units:
        Unit.objects.get_or_create(name=u_name)
    
    # 2. Create Users
    user1, _ = User.objects.get_or_create(username='student_alice')
    user1.set_password('password123')
    user1.save()
    Wallet.objects.get_or_create(user=user1, defaults={'wallet_address': '0xAliceWallet'})
    PersonalProfile.objects.get_or_create(user=user1, defaults={'full_name': 'Alice Wonderland'})
    NFT.objects.get_or_create(user=user1, defaults={'image_ipfs_uri': 'QmHash123'})

    user2, _ = User.objects.get_or_create(username='student_bob')
    user2.set_password('password123')
    user2.save()
    Wallet.objects.get_or_create(user=user2, defaults={'wallet_address': '0xBobWallet'})
    PersonalProfile.objects.get_or_create(user=user2, defaults={'full_name': 'Bob Builder'})

    # 3. Create Posts
    u1 = Unit.objects.get(name="Unit 1: Budgeting")
    post1, _ = Post.objects.get_or_create(
        user=user1, 
        unit=u1,
        content="Just learned about the 50/30/20 rule! It's a game changer.",
        defaults={'is_approved': True, 'is_active': True}
    )

    post2, _ = Post.objects.get_or_create(
        user=user2,
        unit=u1,
        content="Does anyone use a specific app for tracking expenses?",
        defaults={'is_approved': True, 'is_active': True}
    )

    # 4. Create Replies
    Reply.objects.get_or_create(
        user=user2,
        post=post1,
        content="I agree! I'm trying to stick to it this month.",
        defaults={'is_approved': True, 'is_active': True}
    )

    print("Database Seed Complete!")

if __name__ == '__main__':
    seed_data()
