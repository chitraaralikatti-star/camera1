import sys
from ast import literal_eval


def bookingDecision(requestHours, priority, existingHours, capacity):
    if capacity <= 0:
        return "INVALID_CAPACITY"

    totalUsage = requestHours + existingHours
    riskScore = (totalUsage / capacity) * 100 - (priority * 5)

    if riskScore < 50:
        return "APPROVED"
    elif riskScore <= 75:
        return "CONDITIONAL"
    else:
        return "REJECTED"


def get_camera_booking_details(args):
    # DEFAULT VALUES (Docker / Jenkins automatic run)
    cameraId = "CAM-DEFAULT"
    requestHours = 2
    priority = 1
    existingHours = 3
    capacity = 10
    source = "DEFAULT"

    # PARAMETERS FROM Jenkins / CLI (ELSE CASE)
    if len(args) == 6:
        cameraId = args[1]
        requestHours = literal_eval(args[2])
        priority = literal_eval(args[3])
        existingHours = literal_eval(args[4])
        capacity = literal_eval(args[5])
        source = "PARAMETERS"

    result = bookingDecision(requestHours, priority, existingHours, capacity)

    return {
        "CameraID": cameraId,
        "RequestHours": requestHours,
        "Priority": priority,
        "ExistingHours": existingHours,
        "Capacity": capacity,
        "Status": result,
        "Source": source
    }


def display_result(data):
    return [
        f"Input Source   : {data['Source']}",
        f"Camera ID      : {data['CameraID']}",
        f"Request Hours : {data['RequestHours']}",
        f"Priority      : {data['Priority']}",
        f"Existing Hours: {data['ExistingHours']}",
        f"Capacity      : {data['Capacity']}",
        f"Booking Status: {data['Status']}"
    ]


if __name__ == "__main__":
    data = get_camera_booking_details(sys.argv)
    output = display_result(data)

    for line in output:
        print(line)
