from typing import Any
from Website.models import Post,Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts Post data"

    def handle(self, *args: Any, **options: Any) -> str | None:
        
        # delete existing data
        Post.objects.all().delete()
        
        titles = [
                "The Future of AI",
                "Climate Change Solutions",
                "Remote Work Trends",
                "Quantum Computing Explained",
                "Renewable Energy Innovations",
                "Deep Learning Demystified",
                "Post-Pandemic Economic Outlook",
                "Blockchain in Finance",
                "Storytelling in Marketing",
                "Medical Technology Advances"
                "Space Exploration Challenges"
                "Psychology of Decision Making",
                "Evolution of Social Media",
                ]

        contents = [
            "Exploring the future of artificial intelligence and its impact on society.",
            "Discovering solutions to combat climate change and protect the environment.",
            "Analyzing trends and challenges in remote work environments.",
            "An introduction to the principles and applications of quantum computing",
            "Investigating the latest innovations in renewable energy sources.",
            "Understanding the fundamentals of deep learning and neural networks.",
            "Examining the economic landscape in the aftermath of the COVID-19 pandemic",
            "Harnessing the power of storytelling to create compelling marketing campaign",
            "Highlighting breakthroughs and advancements in medical technology.",
            "Examining the effects of globalization on local and global economies."
            "Embracing mindfulness practices for enhanced well-being and productivity.",
            "Revolutionizing education through online learning platforms and resources.",
            "Exploring the intersection of art, design, and technology in the digital age."

            ]

        img_urls = [
            "https://picsum.photos/id/1/700/350",
            "https://picsum.photos/id/2/700/350",
            "https://picsum.photos/id/3/700/350",
            "https://picsum.photos/id/4/700/350",
            "https://picsum.photos/id/5/700/350",
            "https://picsum.photos/id/6/700/350",
            "https://picsum.photos/id/7/700/350",
            "https://picsum.photos/id/8/700/350",
            "https://picsum.photos/id/9/700/350",
            "https://picsum.photos/id/10/700/350",
            "https://picsum.photos/id/11/700/350",
            "https://picsum.photos/id/12/700/350",
            "https://picsum.photos/id/13/700/350",
        ]
        
        categories = Category.objects.all()

        for title , content ,img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,image=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        