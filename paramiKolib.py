import paramiko
import getpass


host = input("Enter host  ") 
port = int(input("Enter port"))
username = input("Enter username: ")
password = getpass.getpass("Enter password (hidden): ")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    
    ssh.connect(
        hostname=host,
        port=port,
        username=username,
        password=password,
        allow_agent=False,
        look_for_keys=False,
        timeout=10
    )
    print(" Connected successfully!\n")

    
    commands = ["whoami", "pwd", "ls"]

    for cmd in commands:
        print(f" Running: {cmd}")
        stdin, stdout, stderr = ssh.exec_command(cmd)

    
        output = stdout.read().decode().strip()
        
        error = stderr.read().decode().strip()

        
        if output:
            print("Output:\n", output)
        if error:
            print("Error:\n", error)
        print("-" * 40)

except paramiko.AuthenticationException:
    print(" Authentication failed! Check username/password.")
except paramiko.SSHException as e:
    print(" SSH error:", str(e))
except Exception as e:
    print(" Other error:", str(e))
finally:
    ssh.close()
    print("\n Connection closed.")
