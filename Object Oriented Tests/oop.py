import datetime

class user:

    def __init__(self, name, last_logged_in_at = None):
        self.name = name
        self.is_logged_in = False
        self.last_logged_in_at = last_logged_in_at

    def name(self, user1):
        return self.name
      
    def name(self, value):
        self.name = value 

    def is_logged_in_at(self):
        return self.is_logged_in_at

    def last_logged_in_at(self):
        return self.last_logged_in_at 

    def log_in(self):
        self.is_logged_in = True
        self.last_logged_in_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


    def log_out(self):
        self.is_logged_in = False
        

    def can_edit(self, comment):
        if comment.author.name == self.name:
            return True
        else:
            return False

    def can_delete(self, comment):
        return False

class moderator(user):
    def __init__(self, name):
        user.__init__(self, name)

    def can_delete(self, comment):
        return True



class admin(moderator):

    def __init__(self, name):
        moderator.__init__(self, name)

    def can_edit(self, comment):
        return True 


class comment:
    def __init__(self, author, message, replied_to = None, created_at = None):
        self.created_at = datetime.datetime.now()
        self.author = author
        self.message = message
        self.replied_to = replied_to
        

    def author(self):
        return self._author

    def author(self, value):
        self.author = value

    def message(self):
        return self.message

    def message(self, value):
        self.message = value

    def created_at(self):
        return self.created_at

    def replied_to(self):
        return self.replied_to

    def replied_to(self, value):
        self.replied_to = value

    def to_string(self):
        if self.replied_to == None:
          return self.message + " by " + self.author.name
        else:
          return self.message + " by " + self.author.name + " (replied to {})".format(self.replied_to.author.name)