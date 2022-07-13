import json

class Change:
    __body = dict()
   
    def __init__(self, branch_name, commit_id, comment):
        self.branch_name = branch_name
        self.commit_id = commit_id
        self.comment = comment

    def add_content(self, path, content):
        '''
        path = the path to the file including the parent folder\n\r
        content = the changes being made to the file
        '''
        self.__body.update({path:content})

    def __refupdates(self):
        '''
        the incoming parameter should be in a dictionary
        with the format of {branch_name: branch, commit_id: commit id}
        '''
        refupdate = {"refUpdates": [{"name": f"refs/heads/{self.branch_name}","oldObjectId": f"{self.commit_id}"}]}

        return refupdate

    def __commits(self):
        '''
        return a list of dictionaries
        '''
        list_of_changes = []

        content = self.__body
        for k,v in content.items():
            my_changes =  {
            "changeType": "edit",
            "item": {
                "path": f"/{k}"
            },
            "newContent": {
                "content": f"{v}",
                "contentType": "rawtext"
            }}

            list_of_changes.append(my_changes)

        return list_of_changes

    def git_push(self):
        changed_items = ["".join(json.dumps(item)) for item in self.__commits()]
        return json.dumps(self.__refupdates())[0:-1] + ", \"commits\": [{\"comment\": \"" + self.comment + "\",\"changes\": [".join(changed_items) + "]}]}"

        

