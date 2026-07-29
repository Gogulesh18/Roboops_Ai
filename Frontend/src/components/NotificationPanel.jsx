export default function NotificationPanel({ robots = [] }) {

    const notifications = [];

    robots.forEach(robot => {

        if (robot.battery < 20) {

            notifications.push({
                icon: "🔋",
                text: `${robot.id} battery is low`
            });

        }

        if (robot.temperature > 45) {

            notifications.push({
                icon: "🌡️",
                text: `${robot.id} temperature is high`
            });

        }

        if (robot.status === "Charging") {

            notifications.push({
                icon: "⚡",
                text: `${robot.id} is charging`
            });

        }

    });

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-6">

                🔔 Notifications

            </h2>

            {

                notifications.length === 0

                    ?

                    (

                        <p className="text-green-600">

                            ✅ No Alerts

                        </p>

                    )

                    :

                    (

                        <div className="space-y-3">

                            {

                                notifications.map((item, index) => (

                                    <div
                                        key={index}
                                        className="bg-slate-100 rounded-xl p-4 flex gap-3"
                                    >

                                        <span className="text-2xl">

                                            {item.icon}

                                        </span>

                                        <span>

                                            {item.text}

                                        </span>

                                    </div>

                                ))

                            }

                        </div>

                    )

            }

        </div>

    );

}
