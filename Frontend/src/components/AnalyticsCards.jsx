export default function AnalyticsCards({ dashboard }) {

    const analytics = [

        {
            title: "Fleet Utilization",
            value: `${dashboard.fleet_utilization}%`,
            icon: "📊",
            color: "bg-blue-500"
        },

        {
            title: "Average Battery",
            value: `${dashboard.average_battery}%`,
            icon: "🔋",
            color: "bg-green-500"
        },

        {
            title: "Average Temperature",
            value: `${dashboard.average_temperature}°C`,
            icon: "🌡️",
            color: "bg-red-500"
        },

        {
            title: "Low Battery Robots",
            value: dashboard.low_battery_robots,
            icon: "⚠️",
            color: "bg-yellow-500"
        },

        {
            title: "Traffic Level",
            value: dashboard.traffic_level,
            icon: "🚦",
            color: "bg-purple-500"
        },

        {
            title: "Queued Tasks",
            value: dashboard.queued_tasks,
            icon: "📦",
            color: "bg-indigo-500"
        },

        {
            title: "Collisions",
            value: dashboard.collisions,
            icon: "💥",
            color: "bg-pink-500"
        },

        {
            title: "Maintenance Needed",
            value: dashboard.maintenance_needed,
            icon: "🛠️",
            color: "bg-orange-500"
        }

    ];

    return (

        <div className="mt-12">

            <h2 className="text-3xl font-bold mb-6">

                📈 Fleet Analytics

            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

                {analytics.map((item) => (

                    <div
                        key={item.title}
                        className={`${item.color} text-white rounded-2xl shadow-lg p-6`}
                    >

                        <div className="flex justify-between items-center">

                            <div>

                                <p className="text-sm opacity-80">

                                    {item.title}

                                </p>

                                <h2 className="text-3xl font-bold mt-2">

                                    {item.value}

                                </h2>

                            </div>

                            <div className="text-4xl">

                                {item.icon}

                            </div>

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}