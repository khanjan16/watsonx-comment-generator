import os
import requests
import glob
import json
from git import Repo
from dotenv import load_dotenv
from os.path import join, dirname

error_file_count = 0
success_file_count = 0


def prepare_data_to_send3(file_content, generated_content):
    data = {
        "model_id": "meta-llama/llama-2-70b",
        "inputs": [
            "Example Java Class: \n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent; \nimport org.kohsuke.github.GHRepository; \nimport org.kohsuke.github.GitHub; \n\nimport java.io.IOException; \n\npublic class GitHubIntegrationBranchReader { \n    public static void main(String[] args) { \n        String repositoryOwner = \"your-repository-owner\"; \n        String repositoryName = \"your-repository-name\"; \n        String branchName = \"integration\"; \n  \n        try { \n            // Authenticate to GitHub using your personal access token or credentials \n            // Replace \"your-github-token\" with your actual GitHub token or username and password \n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\"); \n            // Get the repository by owner and name \n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName); \n            // Get the content of the \"integration\" branch \n            GHContent content = repository.getFileContent(\"/\", branchName); \n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the '\''integration'\'' branch:\"); \n            System.out.println(content.getContent()); \n        } catch (IOException e) { \n            e.printStackTrace(); \n        } \n    } \n} \n\n \nExample Java Class with Comments: \n\n{Class}\n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent;\nimport org.kohsuke.github.GHRepository;\nimport org.kohsuke.github.GitHub;\n\nimport java.io.IOException;\n\n/**\n * This class demonstrates how to read the content of the \"integration\" branch from a GitHub repository using the GitHub API.\n */\npublic class GitHubIntegrationBranchReader {\n\n    /**\n     * The main method that reads the content of the \"integration\" branch from the specified GitHub repository.\n     *\n     * @param args Command-line arguments (not used in this example).\n     */\n    public static void main(String[] args) {\n        // Replace these variables with the appropriate values for the GitHub repository you want to read\n        String repositoryOwner = \"your-repository-owner\";\n        String repositoryName = \"your-repository-name\";\n        String branchName = \"integration\";\n\n        try {\n            // Authenticate to GitHub using your personal access token or credentials\n            // Replace \"your-github-token\" with your actual GitHub token or username and password\n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\");\n\n            // Get the repository by owner and name\n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName);\n\n            // Get the content of the \"integration\" branch\n            GHContent content = repository.getFileContent(\"/\", branchName);\n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the '\''integration'\'' branch:\");\n            System.out.println(content.getContent());\n        } catch (IOException e) {\n            e.printStackTrace();\n        }\n    }\n}\n\n{/Class}\n\nActual Java Class: \n\n"
            + file_content + "\n Actual Java Class with Comments: \n{Class}" + generated_content
        ],
        "parameters": {
            "decoding_method": "sample",
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 50,
            "typical_p": 1,
            "random_seed": 1,
            "repetition_penalty": 1,
            "min_new_tokens": 1,
            "max_new_tokens": 400,
            "moderations": {
                "hap": {
                    "input": True,
                    "threshold": 0.75,
                    "output": True
                }
            }
        }
    }
    return data


def prepare_data_to_send2(file_content, generated_content):
    data = {
        "model_id": "bigcode/starcoder",
        "inputs": [
            "Example Java Class: \n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent; \nimport org.kohsuke.github.GHRepository; \nimport org.kohsuke.github.GitHub; \n\nimport java.io.IOException; \n\npublic class GitHubIntegrationBranchReader { \n    public static void main(String[] args) { \n        String repositoryOwner = \"your-repository-owner\"; \n        String repositoryName = \"your-repository-name\"; \n        String branchName = \"integration\"; \n  \n        try { \n            // Authenticate to GitHub using your personal access token or credentials \n            // Replace \"your-github-token\" with your actual GitHub token or username and password \n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\"); \n            // Get the repository by owner and name \n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName); \n            // Get the content of the \"integration\" branch \n            GHContent content = repository.getFileContent(\"/\", branchName); \n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the '\''integration'\'' branch:\"); \n            System.out.println(content.getContent()); \n        } catch (IOException e) { \n            e.printStackTrace(); \n        } \n    } \n} \n\n \nExample Java Class with Comments: \n\n{Class}\n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent;\nimport org.kohsuke.github.GHRepository;\nimport org.kohsuke.github.GitHub;\n\nimport java.io.IOException;\n\n/**\n * This class demonstrates how to read the content of the \"integration\" branch from a GitHub repository using the GitHub API.\n */\npublic class GitHubIntegrationBranchReader {\n\n    /**\n     * The main method that reads the content of the \"integration\" branch from the specified GitHub repository.\n     *\n     * @param args Command-line arguments (not used in this example).\n     */\n    public static void main(String[] args) {\n        // Replace these variables with the appropriate values for the GitHub repository you want to read\n        String repositoryOwner = \"your-repository-owner\";\n        String repositoryName = \"your-repository-name\";\n        String branchName = \"integration\";\n\n        try {\n            // Authenticate to GitHub using your personal access token or credentials\n            // Replace \"your-github-token\" with your actual GitHub token or username and password\n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\");\n\n            // Get the repository by owner and name\n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName);\n\n            // Get the content of the \"integration\" branch\n            GHContent content = repository.getFileContent(\"/\", branchName);\n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the '\''integration'\'' branch:\");\n            System.out.println(content.getContent());\n        } catch (IOException e) {\n            e.printStackTrace();\n        }\n    }\n}\n\n{/Class}\n\nActual Java Class: \n\n"
            + file_content + "\n Actual Java Class with Comments: \n{Class}" + generated_content
        ],
        "parameters": {
            "decoding_method": "sample",
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 50,
            "typical_p": 1,
            "random_seed": 1,
            "repetition_penalty": 1,
            "min_new_tokens": 1,
            "max_new_tokens": 400,
            "moderations": {
                "hap": {
                    "input": True,
                    "threshold": 0.75,
                    "output": True
                }
            }
        }
    }
    return data


def prepare_data_to_send1(file_content, generated_content):
    data = {
        "model_id": "bigcode/starcoder",
        "inputs": [
            "Example Java Class: \n\n \n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent; \nimport org.kohsuke.github.GHRepository; \nimport org.kohsuke.github.GitHub; \n\nimport java.io.IOException; \n\npublic class GitHubIntegrationBranchReader { \n    public static void main(String[] args) { \n        String repositoryOwner = \"your-repository-owner\"; \n        String repositoryName = \"your-repository-name\"; \n        String branchName = \"integration\"; \n  \n        try { \n            // Authenticate to GitHub using your personal access token or credentials \n            // Replace \"your-github-token\" with your actual GitHub token or username and password \n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\"); \n            // Get the repository by owner and name \n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName); \n            // Get the content of the \"integration\" branch \n            GHContent content = repository.getFileContent(\"/\", branchName); \n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the 'integration' branch:\"); \n            System.out.println(content.getContent()); \n        } catch (IOException e) { \n            e.printStackTrace(); \n        } \n    } \n} \n\n \nExample Java Class with Comments: \n\n{CLASS}\n\n/** \n * IBM Confidential - OCO Source Materials \n * Copyright (c) IBM Corp. 1992, 2023 \n * Copyright (c) Internet Security Systems, Inc. 1992-2006 \n * The source code for this program is not published or otherwise divested of its trade secrets, \n * irrespective of what has been deposited with the U.S. Copyright Office. \n */ \nimport org.kohsuke.github.GHContent;\nimport org.kohsuke.github.GHRepository;\nimport org.kohsuke.github.GitHub;\n\nimport java.io.IOException;\n\n/**\n * This class demonstrates how to read the content of the \"integration\" branch from a GitHub repository using the GitHub API.\n */\npublic class GitHubIntegrationBranchReader {\n\n    /**\n     * The main method that reads the content of the \"integration\" branch from the specified GitHub repository.\n     *\n     * @param args Command-line arguments (not used in this example).\n     */\n    public static void main(String[] args) {\n        // Replace these variables with the appropriate values for the GitHub repository you want to read\n        String repositoryOwner = \"your-repository-owner\";\n        String repositoryName = \"your-repository-name\";\n        String branchName = \"integration\";\n\n        try {\n            // Authenticate to GitHub using your personal access token or credentials\n            // Replace \"your-github-token\" with your actual GitHub token or username and password\n            GitHub github = GitHub.connectUsingOAuth(\"your-github-token\");\n\n            // Get the repository by owner and name\n            GHRepository repository = github.getRepository(repositoryOwner + \"/\" + repositoryName);\n\n            // Get the content of the \"integration\" branch\n            GHContent content = repository.getFileContent(\"/\", branchName);\n\n            // Print the content of the \"integration\" branch\n            System.out.println(\"Content of the 'integration' branch:\");\n            System.out.println(content.getContent());\n        } catch (IOException e) {\n            e.printStackTrace();\n        }\n    }\n}\n\n {/CLASS}\n\nActual Java Class: \n\n"
            + file_content + "\n Actual Java Class with Comments: \n" + generated_content
        ],
        "parameters": {
            "decoding_method": "sample",
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 50,
            "typical_p": 1,
            "random_seed": 1,
            "repetition_penalty": 1,
            "min_new_tokens": 1,
            "max_new_tokens": 300,
            "moderations": {
                "hap": {
                    "input": True,
                    "threshold": 0.75,
                    "output": True
                }
            }
        }
    }
    return data


def get_processed_content(generated_content):
    # Don't know what would be the end token may be "'''" or "{/Class}"
    if generated_content.find(end_token) != -1:
        processed_content = generated_content[0:generated_content.find(end_token)]
    if generated_content.find(end_token_class) != -1:
        processed_content = generated_content[0:generated_content.find(end_token_class)]
    # processed_content = processed_content.encode().decode('unicode_escape')
    processed_content = processed_content.strip()
    return processed_content


def send_java_file_content(file_path, file_content, previous_content, model_choice):
    bam_token = ""
    WATSONX_TOKEN = os.environ.get('WATSONX_TOKEN')
    WATSONX_URL = os.environ.get('WATSONX_URL')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + WATSONX_TOKEN
    }

    data = None
    if (model_choice.lower() == "star"):
        data = prepare_data_to_send2(file_content, previous_content)
    else:
        data = prepare_data_to_send3(file_content, previous_content)
    #print(WATSONX_URL)

    response = requests.post(WATSONX_URL, json=data, headers=headers)

    if response.status_code == 200:
        print("Comment Generation is In Progress ...")
        # print("Response content:")
        resp_data = response.json()
        generated_text = resp_data["results"][0]["generated_text"]
        generated_content = previous_content + generated_text
        # print(generated_content)
        if generated_content.find(end_token_class) == -1 and generated_content.find(end_token) == -1:
            # If half response generated, call again with
            send_java_file_content(file_path, file_content, generated_content, model_choice)
        else:
            # final_content = json.dumps(generated_content, indent=2)
            processed_content = get_processed_content(generated_content)
            # print("\n\nFinal output:\n")
            # print(processed_content)
            global success_file_count
            success_file_count += 1
            write_response_to_file(file_path, processed_content)
    else:
        print(f"API request failed with status code {response.status_code}.")
        print("Response content:")
        print(response.text)
        global error_file_count
        error_file_count +=1

def write_response_to_file(file_path, response_content):
    # new_file_path = file_path.replace(".java", "_new.java")
    new_file_path = file_path
    with open(new_file_path, 'w') as new_file:
        new_file.write(response_content)

end_token = "'''"
end_token_class = "{/Class}"

def generateComment(path):
    local_directory = path
    model_choice = 'lama'
    model_choice = input(
        'Choose the model needs to be used to generate Comments (lama or star)(lama is default model)?\n')
    java_files = glob.glob(os.path.join(local_directory, '**', '*.java'), recursive=True)
    totalFiles = len(java_files)
    presentFileIndex = 0
    print("Total Java files found : ", totalFiles)

    skipped_file_count = 0

    for java_file in java_files:
        presentFileIndex = presentFileIndex + 1
        print("File ", presentFileIndex, "/", totalFiles, ", \n\tname : " + java_file)
        if java_file.endswith("Test.java") or java_file.find("src\\test\\java") != -1:
            print("\tskipping file.")
            skipped_file_count += 1
            # Skip files ending with "Test.java"
            continue
        # if presentFileIndex > 3:
        #     continue
        with open(java_file, 'r') as file:
            file_size = os.path.getsize(java_file)
            content = file.read()
            print("\tcontent extracted with size : ", file_size)
        response_content = send_java_file_content(java_file, content, "", model_choice)
        # break
        # if response_content is not None:
        # write_response_to_file(java_file, response_content)

    print("Task completed!")
    print("-------------Task Summary------------")
    print(" Branch Name : comment_generation ")
    print(" SuccessFully Generated Comments for file(s) :", success_file_count)
    print(" Recieved Error While Generating comments for no of file(s) :", error_file_count)
    print(" Skipped File(s) : ", skipped_file_count)
    print("-------------------------------------")


def clone_repo_and_checkout_branch(repo_url, local_path, branch_name):
    if os.path.exists(local_path):
        print("Local path already exists. Skipping cloning.")
        try:
            repo = Repo(local_path)
            try:
                #print("checkingout branch")
                repo.git.checkout('-b', branch_name)
            except:
                try:
                    #print('checkout branch2')
                    repo.git.checkout(branch_name)
                except:
                    getInput()
        except:
            getInput()
    else:
        print(f"Cloning repository repository to {local_path}")
        Repo.clone_from(repo_url, local_path)
        try:
            repo = Repo(local_path)
            try:
                repo.git.checkout('-b', branch_name)
            except git.exc.GitCommandError:
                try:
                    repo.git.checkout(branch_name)
                except:
                    getInput()
        except:
            getInput()
    print(f"Checked out branch '{branch_name}' at {local_path}")


def commit_changes(local_path):
    repo = Repo(local_path)
    EMAIL = os.environ.get('EMAIL')
    repo.git.add(all=True)
    repo.git.commit('-m', 'comments generation', author=EMAIL)

    print('..changes commited...')

    origin = repo.remote('origin')
    repo.remotes.origin.push(all=True)

    print('..changes pushed..')

def getInput():
    dotenv_path = join(dirname(__file__), '.env')

    load_dotenv(dotenv_path)
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

    repo_name = input('which repository you want to work upon under Managed-Security Workspace?\n')
    github_repo_url = "https://github.ibm.com/managed-security/" + repo_name + ".git"
    github_repo_url_with_token = github_repo_url.replace("https://", f"https://oauth2:{GITHUB_TOKEN}@")
    DIR = os.environ.get('LOCAL_PATH')
    local_path = DIR + repo_name
    branch_name = "comment_generation"

    clone_repo_and_checkout_branch(github_repo_url_with_token, local_path, branch_name)
    generateComment(local_path)
    commit_changes(local_path)

def main():
    getInput()

if __name__ == "__main__":
    main()
