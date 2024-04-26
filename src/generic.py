# This is the main file to hold common functions/classes
import uuid


def generate_uuid():
    return str(uuid.uuid4())


def format_social_media_links(socials):
    formatted_socials = {}
    if "instagram" in socials and socials["instagram"]:
        formatted_socials["Instagram"] = {
            "url": f"https://www.instagram.com/{socials['instagram']}",
            "icon": "fab fa-instagram",
        }
    if "tiktok" in socials and socials["tiktok"]:
        formatted_socials["TikTok"] = {
            "url": f"https://www.tiktok.com/@{socials['tiktok']}",
            "icon": "fab fa-tiktok",
        }
    if "twitter" in socials and socials["twitter"]:
        formatted_socials["Twitter"] = {
            "url": f"https://twitter.com/{socials['twitter']}",
            "icon": "fab fa-twitter",
        }
    if "bandcamp" in socials and socials["bandcamp"]:
        formatted_socials["Bandcamp"] = {
            "url": f"https://{socials['bandcamp']}.bandcamp.com/",
            "icon": "fab fa-bandcamp",
        }
    if "soundcloud" in socials and socials["soundcloud"]:
        formatted_socials["SoundCloud"] = {
            "url": f"https://soundcloud.com/{socials['soundcloud']}",
            "icon": "fab fa-soundcloud",
        }
    if "youtube" in socials and socials["youtube"]:
        formatted_socials["YouTube"] = {
            "url": f"https://www.youtube.com/{socials['youtube']}",
            "icon": "fab fa-youtube",
        }
    if "spotify" in socials and socials["spotify"]:
        formatted_socials["Spotify"] = {
            "url": f"https://open.spotify.com/user/{socials['spotify']}",
            "icon": "fab fa-spotify",
        }

    return formatted_socials
