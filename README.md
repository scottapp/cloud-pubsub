# Google Cloud PubSub Example

## Setup

```bash
export PROJECT_ID=YOUR_PROJECT_ID
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-sub --topic my-topic
```

## Running
- run subscriber first, then publisher

## Clean Up
- delete my-topic, my-sub in the google cloud console after testing
