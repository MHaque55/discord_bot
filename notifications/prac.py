import scrapetube

latest = []
videos = scrapetube.get_channel("UCWiY6fYdxuEe78r-0uFCnhA")

for video in videos:
    if video['videoId'] not in latest:
        latest.append(video['videoId'])
        print(f"youtube.com/watch?v={video['videoId']}&ab_channel=LongBeachGriffy")
    break
