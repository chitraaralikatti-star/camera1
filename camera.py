import sys

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

    # PARAMETERS FROM Jenkins / CLI
    if len(args) == 6:
        cameraId = args[1]
        requestHours = int(args[2])
        priority = int(args[3])
        existingHours = int(args[4])
        capacity = int(args[5])

    result = bookingDecision(requestHours, priority, existingHours, capacity)

    return {
        "CameraID": cameraId,
        "Status": result
    }


def display_result(data):
    return [
        f"Camera ID      : {data['CameraID']}",
        f"Booking Status : {data['Status']}"
    ]


if __name__ == "__main__":
    data = get_camera_booking_details(sys.argv)
    output = display_result(data)

    for line in output:
        print(line)
