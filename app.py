from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to calculate BMI and return category + weekly gym plan
def get_bmi_plan(weight, height_cm):
    height_m = height_cm / 100
    bmi = round(weight / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
        plan = {
            "Monday": "Full Body Strength Training",
            "Tuesday": "Light Cardio (20 mins) + Upper Body",
            "Wednesday": "Leg Day + Core",
            "Thursday": "Rest / Stretching",
            "Friday": "Full Body Strength + Core",
            "Saturday": "Yoga or Walking",
            "Sunday": "Rest"
        }
    elif 18.5 <= bmi < 25:
        category = "Normal"
        plan = {
            "Monday": "Push Day (Chest, Shoulders, Triceps)",
            "Tuesday": "Cardio (Jogging or Cycling)",
            "Wednesday": "Pull Day (Back, Biceps)",
            "Thursday": "Core + Flexibility",
            "Friday": "Leg Day",
            "Saturday": "Full Body HIIT",
            "Sunday": "Rest"
        }
    elif 25 <= bmi < 30:
        category = "Overweight"
        plan = {
            "Monday": "Cardio (30 mins) + Light Core",
            "Tuesday": "Bodyweight Circuit Training",
            "Wednesday": "Cardio (Brisk Walk) + Upper Body",
            "Thursday": "Yoga / Stretching",
            "Friday": "HIIT + Core",
            "Saturday": "Lower Body + Cardio",
            "Sunday": "Rest"
        }
    else:
        category = "Obese"
        plan = {
            "Monday": "Walking (30 mins)",
            "Tuesday": "Light Cardio + Mobility",
            "Wednesday": "Bodyweight Strength (Slow Pace)",
            "Thursday": "Rest / Stretch",
            "Friday": "Low Impact HIIT",
            "Saturday": "Yoga / Breathing Exercises",
            "Sunday": "Rest"
        }

    return {
        "bmi": bmi,
        "category": category,
        "weekly_plan": plan
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-plan", methods=["GET","POST"])
def generate_plan():
    data = request.get_json()
    weight = data.get("weight")
    height = data.get("height")

    try:
        weight = float(weight)
        height = float(height)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

    # Calculate BMI
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    # Determine category and gym plan
    if bmi < 18.5:
        category = "Underweight"
        plan_dict = {
            "Monday": "Full-body strength training",
            "Tuesday": "Rest",
            "Wednesday": "Upper body workout",
            "Thursday": "Yoga or light cardio",
            "Friday": "Lower body workout",
            "Saturday": "Core & functional training",
            "Sunday": "Rest"
        }
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        plan_dict = {
            "Monday": "Strength training (push)",
            "Tuesday": "Cardio (HIIT)",
            "Wednesday": "Strength training (pull)",
            "Thursday": "Active recovery (walk/yoga)",
            "Friday": "Leg day",
            "Saturday": "Full-body functional",
            "Sunday": "Rest"
        }
    else:
        category = "Overweight"
        plan_dict = {
            "Monday": "Cardio (brisk walk/jog)",
            "Tuesday": "Strength training (upper)",
            "Wednesday": "Cardio (cycling/swim)",
            "Thursday": "Rest or yoga",
            "Friday": "Strength training (lower)",
            "Saturday": "Cardio + core",
            "Sunday": "Rest"
        }
    plan = [f"{day}: {routine}" for day, routine in plan_dict.items()]
    return jsonify({"bmi": bmi, "plan": plan})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
