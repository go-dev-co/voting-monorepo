# Cats Vs. Dogs: Simple Voting App
Which is better? Cats or dogs? 
To answer this question, I've built a microservices application
which can accept votes from individual users. This is a simple proof of concept app. 
I'll be adding more features as time progresses (unique user accounts, authentication services, and better analytics)

## Design
- The frontend app is hosted and managed on a fastAPI Server
- A reddis queue is used to broker messages between the frontend and worker node
- The worker node is written in Golang. It processes the transactions, and pushes them to a 
postgres database
- A Results app, created with node.js and react, accesses the postgres db and displays results.


## Other notable features.
For each application, a Github CI/CD Pipeline has been created for the following tasks:
- Linting / Code reviewing the application
- Building the application
- Testing the application with unit tests
- Dockerizing and submitting the application to an ECR repository.

Kubernetes is used to orchestarte the application:
- Each service is managed by a deployment.
- There are two services, for each datbase to orchstarte interprocess communication
- Secrets are mangaged by AWS Secret Manager

Terraform is used to deploy infrastructure:
- the kubernetes cluster, ecr repo, and network setup is defined by terraform. 
- A pipeline specifically for terraform will be crated with github actions. 

