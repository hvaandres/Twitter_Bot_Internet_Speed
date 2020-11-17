from TwitterAPI import TwitterAPI
import speedtest
import sched
import time
import os


# Sign up for a developer account with Twitter and create an app to make sure you can get the API_Keys
consumer_key = os.getenv("")
consumer_secret = os.getenv(
    "")
access_token_key = os.getenv(
    "")
access_token_secret = os.getenv(
    "")

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)


# Let's check our internet speed

def my_internet_speed():
    speedtester = speedtest.Speedtest()

    advertised_download = 60
    advertised_upload = 2

    # returned as bits, converted to megabits
    download_speed = int(speedtester.download() / 1000000)
    upload_speed = int(speedtester.upload() / 1000000)

    print("My Download Speed is: " + str(download_speed) + "Mbps")
    print("My Upload Speed is: " + str(upload_speed) + "Mbps")
    print("\n")

# # Uncomment code to create triaged messaging
# thresholds = {'first':0.8, 'second':0.5}
# messages = {'first':'[enter polite message]', 'second': '[enter stern message]'}
# if download_speed < advertised_download * thresholds['first'] or upload_speed < advertised_upload * thresholds['first']:
#     tweet = messages['first']
#     api.request("statuses/update", {"status": tweet})
# elif download_speed < advertised_download * thresholds['second'] or upload_speed < advertised_upload * thresholds['second']:
#     tweet = messages['second']
#     api.request("statuses/update", {"status": tweet})

# If using triaged messaging, above, then comment out the conditional block, below.
    if download_speed < advertised_download * 0.8 or upload_speed < advertised_upload * 0.8:
        tweet = "@google My speeds are 35% slower than advertised, Could you fix this issue? 😊"
        api.request("statuses/update", {"status": tweet})


scheduler = sched.scheduler(time.time, time.sleep)

# Let's check our connection multiple times to see if we can catch a slowdown from your internet to start complaining


def checker_multiple_times(scheduler, interval, action, arguments=()):
    scheduler.enter(interval, 1, checker_multiple_times,
                    (scheduler, interval, action, arguments))
    action()


checker_multiple_times(scheduler, 1, my_internet_speed)
scheduler.run()
