from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

app = Flask(__name__)

# Google Drive Folder IDs for the three galleries
BS_FOLDER_ID = '1M3po0W4Bg'
HC_FOLDER_ID = '187MV5PLY'
MH_FOLDER_ID = '1eQn9hCS6'
NI_FOLDER_ID = '1Kkt-_1ni'
RC_FOLDER_ID = '1U1aCKpJg'
WC_FOLDER_ID = '1mL9ZT5Uv'
SN_FOLDER_ID = '1jPmcOvxF'

# bg-colors = {
#     bg-BS:#c5c3ee,
#     bg-HC:#ffae4d,
#     bg-MH:#ffb3d1,
#     bg-NI:#bcf6d0,
#     bg-RC:#a6b4d9,
#     bg-WC:#fbefd5,
#     bg-SN:#a6b4d9
# }

# sidebar-colors = {
#     BS:#2b278b,
#     HC:#e67d00,
#     MH:#800033,
#     NI:#09431d,
#     RC:#131a2c,
#     WC:#c77e52,
#     SN:#131a2c
# }


# Google Drive API setup
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDS_FILENAME = 'credentials.json' 
TOKEN_FILENAME = 'token.json'

def create_service():
    creds = None
    if os.path.exists(TOKEN_FILENAME):
        creds = Credentials.from_authorized_user_file(TOKEN_FILENAME, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILENAME, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILENAME, 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

drive_service = create_service()

def get_google_drive_images(folder_id, page_token=None):
    try:
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents and mimeType contains 'image/' and trashed=false",
            pageSize=30,  # Load 20 images at a time
            fields="nextPageToken, files(id, name)",
            pageToken=page_token
        ).execute()
        items = results.get('files', [])

        next_page_token = results.get('nextPageToken')

        images = [f"https://drive.google.com/thumbnail?id={item['id']}&sz=w500" for item in items]

        return images, next_page_token
    except Exception as error:
        print(f'An error occurred: {error}')
        return [], None

@app.route('/')
def index():
    return redirect(url_for('gallery', gallery_id=1))

@app.route('/gallery/<int:gallery_id>')
def gallery(gallery_id):
    gallery_titles = {
        1: "Bridal Shower",
        2: "Haldi Ceremony",
        3: "Mehindi",
        4: "Nichayadhartam",
        5: "Reception",
        6: "Wedding Ceremony",
        7: "Sangeet Night",
    }

    bg_classes = {
        1: 'bg-BS',
        2: 'bg-HC',
        3: 'bg-MH',
        4: 'bg-NI',
        5: 'bg-RC',
        6: 'bg-WC',
        7: 'bg-SN',
    }

    sidebar_classes = {
        1: 'sidebar-BS',
        2: 'sidebar-HC',
        3: 'sidebar-MH',
        4: 'sidebar-NI',
        5: 'sidebar-RC',
        6: 'sidebar-WC',
        7: 'sidebar-SN',
    }

    gallery_dates = {
        1: "18.08.2024",
        2: "19.08.2024",
        3: "20.08.2024",
        4: "21.08.2024",
        5: "21.08.2024",
        6: "22.08.2024",
        7: "22.08.2024",
    }

    title = gallery_titles.get(gallery_id, "Gallery")
    bg_class = bg_classes.get(gallery_id, 'default-bg')
    sidebar_class = sidebar_classes.get(gallery_id, 'sidebar-default')
    date = gallery_dates.get(gallery_id, "dd.mm.yyyy")

    return render_template('gallery.html', gallery_title=title, gallery_id=gallery_id, bg_class=bg_class, sidebar_class=sidebar_class, gallery_date=date)

@app.route('/load_images/<int:gallery_id>', methods=['GET'])
def load_images(gallery_id):
    folder_id_map = {
        1: BS_FOLDER_ID,
        2: HC_FOLDER_ID,
        3: MH_FOLDER_ID,
        4: NI_FOLDER_ID,
        5: RC_FOLDER_ID,
        6: WC_FOLDER_ID,
        7: SN_FOLDER_ID,
    }

    folder_id = folder_id_map.get(gallery_id)
    page_token = request.args.get('page_token', None)
    images, next_page_token = get_google_drive_images(folder_id, page_token)
    return jsonify(images=images, next_page_token=next_page_token)

if __name__ == '__main__':
    app.run(port=5000, debug=True)