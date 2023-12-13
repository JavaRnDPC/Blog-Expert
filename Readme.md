Create a simple Blog API using Django REST framework. The API should have the following features:

User Authentication:

Use Token Authentication for securing your API.
Allow users to register and obtain an authentication token.
Login to get token
Blog Post Model:

Create a model for Blog Posts with the following fields:
Title (CharField)
Content (TextField)
Author (ForeignKey to User)
Created_at (DateTimeField - automatically set on creation)
Ensure that only authenticated users can create, update, or delete blog posts.
API Endpoints:

Implement the following API endpoints:
List all blog posts (GET /api/posts/)
Retrieve a single blog post by its ID (GET /api/posts/<id>/)
Create a new blog post (POST /api/posts/)
Update a blog post by its ID (PUT /api/posts/<id>/)
Delete a blog post by its ID (DELETE /api/posts/<id>/)
User Profile:

Already created an endpoint to retrieve the profile information of the authenticated user (GET /api/profile/).
1. Create register API so he will be able to register a new user.
2. USer can have 2 types, every user that is registered should have 2 types ex - student and teacher, as soon registration is completed default profile should be created using django singal. 
3. can create one profile API, Teacher and student both can view both profiles but both can edit only their own profile. 