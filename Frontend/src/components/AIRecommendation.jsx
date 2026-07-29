export default function AIRecommendation({ dashboard }) {

    const recommendations = [];

    // Low Battery
    dashboard.robots.forEach(robot => {

        if (robot.battery < 20) {

            recommendations.push({
                icon: "🔋",
                title: "Low Battery",
                message: `${robot.id} battery is ${robot.battery}%. Send it to Charging Station.`
            });

        }

    });

    // Idle Robots
    dashboard.robots.forEach(robot => {

        if (robot.status === "Idle") {

            recommendations.push({
                icon: "🤖",
                title: "Idle Robot",
                message: `${robot.id} is available for a new mission.`
            });

        }

    });

    // High Temperature
    dashboard.robots.forEach(robot => {

        if (robot.temperature > 45) {

            recommendations.push({
                icon: "🌡️",
                title: "High Temperature",
                message: `${robot.id} temperature is ${robot.temperature}°C. Inspect immediately.`
            });

        }

    });

    // Fleet Health
    if (dashboard.fleet_health_score < 70) {

        recommendations.push({
            icon: "⚠️",
            title: "Fleet Health",
            message: "Fleet health is below 70%. Maintenance is recommended."
        });

    }

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-12">

            <div className="flex justify-between items-center mb-6">

                <h2 className="text-2xl font-bold">

                    🤖 AI Operations Assistant

                </h2>

                <span className="text-green-600 font-semibold">

                    Live Analysis

                </span>

            </div>

            {recommendations.length === 0 ? (

                <div className="text-center py-10 text-green-600 font-semibold">

                    ✅ Fleet operating normally

                </div>

            ) : (

                <div className="space-y-4">

                    {recommendations.map((item, index) => (

                        <div
                            key={index}
                            className="flex items-start gap-4 p-4 rounded-xl bg-slate-100"
                        >

                            <div className="text-3xl">

                                {item.icon}

                            </div>

                            <div>

                                <h3 className="font-bold">

                                    {item.title}

                                </h3>

                                <p className="text-gray-600">

                                    {item.message}

                                </p>

                            </div>

                        </div>

                    ))}

                </div>

            )}

        </div>

    );

}