# locustfile.py

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def sleep(self):
        self.client.get("/sleep")

    @task
    def sleep2(self):
        self.client.get("/sleep2")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0  # ms
    max_wait = 1


if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --port=8888 --host=http://localhost")
