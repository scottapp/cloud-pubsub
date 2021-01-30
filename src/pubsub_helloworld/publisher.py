import os
from google.cloud import pubsub_v1


def main():
    project_id = os.getenv('PROJECT_ID', None)
    assert project_id, 'error project id'

    topic_id = 'my-topic'

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    for n in range(1, 10):
        data = "Message number {}".format(n)
        # Data must be a bytestring
        data = data.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())

    print(f"Published messages to {topic_path}.")


if __name__ == '__main__':
    # should do gcloud pubsub topics create my-topic first
    main()
