import xml.etree.ElementTree as ET
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from management.models.add_asset import Asset


def sync_miradore():
    # Check if the previous job is still running
    if sync_miradore.is_running:
        print('Previous job still running, skipping this run')
        return

    # Set the flag to indicate that the current job is running
    sync_miradore.is_running = True

    # Run the job
    print('Running my job...')

    # Reset the flag
    sync_miradore.is_running = False

    # initialize ID to 1
    device_id = 1
    consecutive_404_count = 0

    # loop through each device in Miradore
    while consecutive_404_count < 3:
        # make API request and parse response

        url = f'https://datasafely.online.miradore.com/API/' \
              f'Device/{device_id}?auth=2_Fy5AU84,9xbi]6C&select=*,InvDevice.*,' \
              f'Tag.Name,User.Email,User.LastName,User.FirstName' \
              f'&filters=InvDevice.InventoryTime%20gt%20%2724.06.2014%27&options=dateFormat=dd.MM.yyyy'
        response = requests.get(url)
        # print(response)

        # check if response status code is 404, indicating no device
        if response.status_code == 404:
            consecutive_404_count += 1
            # stop if three consecutive 404 status code is reached
            if consecutive_404_count == 3:
                print("Three consecutive 404 status code reached...")
                break
            # continue if not
            else:
                device_id += 1
                continue
        # reset count if page doesn't show status code 404
        else:
            consecutive_404_count = 0
            # print(f'Device ID: {device_id}')
            xml_content = response.content

            # parse XML content
            root = ET.fromstring(xml_content)

            # check if device is unmanaged
            status_element = root.find('Items/Device/OnlineStatus')
            if status_element is not None:
                status = status_element.text
                if status == 'Unmanaged':
                    device_id += 1
                    continue

            # find model element
            model_element = root.find('Items/Device/InvDevice/Model')
            if model_element is not None:
                model = model_element.text
            else:
                device_id += 1
                continue
            # print(f"Model: {model}")

            # find manufacturer element
            manufacturer_element = root.find('Items/Device/InvDevice/Manufacturer')
            if manufacturer_element is not None:
                manufacturer = manufacturer_element.text
            else:
                device_id += 1
                continue
            # print(f"Manufacturer: {manufacturer}")

            # find email element
            email_element = root.find('Items/Device/User/Email')
            if email_element is not None:
                email = email_element.text
            else:
                device_id += 1
                continue
            # print(f"Email: {email}")

            # find last name element
            last_name_element = root.find('Items/Device/User/Lastname')
            if last_name_element is not None:
                last_name = last_name_element.text
            else:
                device_id += 1
                continue
            # print(f"Last Name: {last_name}")

            # find first name element
            first_name_element = root.find('Items/Device/User/Firstname')
            if first_name_element is not None:
                first_name = first_name_element.text
            else:
                device_id += 1
                continue
            # print(f"First Name: {first_name}")

            # add the retrieved information to the database
            asset = Asset.objects.filter(asset_id=device_id).first()
            # update
            if asset:
                asset.asset_id = device_id
                asset.model = model
                asset.manufacturer = manufacturer
                asset.first_name = first_name
                asset.last_name = last_name
                asset.user_email = email
                asset.save()

            # create
            else:
                Asset.objects.create(
                    asset_id=device_id,
                    model=model,
                    manufacturer=manufacturer,
                    first_name=first_name,
                    last_name=last_name,
                    user_email=email,
                    available_to_borrow=True
                )

            # increment ID for next iteration
            device_id += 1

            print("sync_miradore() has finished...")


def start():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Initialize the flag to indicate that no job is currently running
    sync_miradore.is_running = False

    # Schedule the job to run
    scheduler.add_job(sync_miradore, 'interval', seconds=10)
