channels = []

for i in range(10):
    name = "Canal #" + str(i + 1)
    url = "https://www.youtube.com/channel/" + str(i + 1)
    icon = "/icons/channel_" + str(i + 1) + ".png"

    channels.append({
        "title": name,
        "url": url,
        "thumbnail": icon
    })

for channel in channels:
    addDir(title=channel["title"], url=channel["url"], thumbnail=channel["thumbnail"])
