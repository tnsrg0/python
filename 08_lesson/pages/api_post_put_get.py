import requests


class ApiRequestsYougile:

    def __init__(self, login, password, company_id):
        self.base_url = 'https://ru.yougile.com'
        token = self.get_auth_key(login, password, company_id)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
            }

    def get_auth_key(self, login, password, company_id):
        url = self.base_url + '/api-v2/auth/keys'
        headers = {
            "Content-Type": "application/json"
        }
        request_body = {
            "login": login,
            "password": password,
            "companyId": company_id
            }
        response = requests.request(
            "POST",
            url,
            json=request_body,
            headers=headers
            )
        return response.json().get("key")

    def post_project_creation(self, project_title):
        url = self.base_url + '/api-v2/projects'
        request_body = {
            "title": project_title
            }
        response = requests.request(
            "POST",
            url,
            json=request_body,
            headers=self.headers
            )
        return response

    def get_by_id(self, id):
        url = self.base_url + '/api-v2/projects/' + id
        response = requests.request("GET", url, headers=self.headers)
        return response

    def put_project(self, id, new_title):
        url = self.base_url + '/api-v2/projects/' + id
        request_body = {
            "title": new_title
            }
        response = requests.request(
            "PUT",
            url,
            json=request_body,
            headers=self.headers
            )
        return response
