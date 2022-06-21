import dropbox;
import os;
from dropbox.files import WriteMode;

class TransferData:
    def __init__ (self, access_token):
        self.access_token = access_token;

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token);
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path= os.path.join(root, fileName);
                relative_path= os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

def main():
    accessToken= 'sl.BJ8zxvTTIpuKeHM56Rb7eQ5BivoIEGkWZewr2TA23NoB3qBIj0eCPTPHNWvvIMW-VzuEZsrccKAadLKcmjfBwZCaljMO2ZDjJw0v56cBSiOwgp2tEbYtvvZydPVuiB6awI1dKqg';
    transferData = TransferData(accessToken);

    file_from = input('Enter the path of the file needed to be transfered: ');
    file_to = input('Enter the path of the destination of the transfered file: ');

    transferData.upload_file(file_from, file_to)

    print("Your file ", file_from, " has been successfully transerfered to ", file_to);

main();
