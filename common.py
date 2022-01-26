class AsanaTicket:

    def __init__(self):
        pass

    def create_task(self, client, workspace_id, taskproject ):
        return client.tasks.create_in_workspace(workspace_id,
                                         {'name': self.hostel + '_' + self.room,
                                          'notes': self.trouble,
                                          'projects': [taskproject]
                                         }
                                        )