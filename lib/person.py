APPROVED_JOBS = [
    "Sales",
    "ITC",
    "Engineer",
    "Artist",
    "Manager",
    "Teacher"
]

class Person:
    def __init__(self, name="Guido", job="Sales"):
        self.name = name
        self.job = job

    # name property
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # job property
    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
