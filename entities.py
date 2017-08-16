class Post:
    def __init__(self, post_id, thread_id, user_id, username, post_date, message, ip_id, message_state, attach_count,
                 position, likes, like_users, warning_id, warning_message, last_edit_date, last_edit_user_id,
                 edit_count):
        self.post_id = post_id
        self.thread_id = thread_id
        self.user_id = user_id
        self.username = username
        self.post_date = post_date
        self.message = message
        self.ip_id = ip_id
        self.message_state = message_state
        self.attach_count = attach_count
        self.position = position
        self.likes = likes
        self.like_users = like_users
        self.warning_id = warning_id
        self.warning_message = warning_message
        self.last_edit_date = last_edit_date
        self.last_edit_user_id = last_edit_user_id
        self.edit_count = edit_count

    def bump_position(self):
        self.position = self.position + 1


class Thread:
    def __init__(self, thread_id, node_id, title, reply_count, view_count, user_id, username, post_date, sticky,
                 discussion_state, discussion_open, discussion_type, first_post_id, first_post_likes, last_post_date,
                 last_post_id, last_post_user_id, last_post_username, prefix_id, tags):
        self.thread_id = thread_id
        self.node_id = node_id
        self.title = title
        self.reply_count = reply_count
        self.view_count = view_count
        self.user_id = user_id
        self.username = username
        self.post_date = post_date
        self.sticky = sticky
        self.discussion_state = discussion_state
        self.discussion_open = discussion_open
        self.discussion_type = discussion_type
        self.first_post_id = first_post_id
        self.first_post_likes = first_post_likes
        self.last_post_date = last_post_date
        self.last_post_id = last_post_id
        self.last_post_user_id = last_post_user_id
        self.last_post_username = last_post_username
        self.prefix_id = prefix_id
        self.tags = tags

    def bump_reply_count(self):
        self.reply_count = self.reply_count + 1


class Attachment:
    def __init__(self, attachment_id, data_id, content_type, content_id, attach_date, temp_hash, unassociated,
                 view_count):
        self.attachment_id = attachment_id
        self.data_id = data_id
        self.content_type = content_type
        self.content_id = content_id
        self.attach_date = attach_date
        self.temp_hash = temp_hash
        self.unassociated = unassociated
        self.view_count = view_count