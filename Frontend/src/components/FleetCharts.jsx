import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    PieChart,
    Pie,
    Cell,
    Legend
} from "recharts";

export default function FleetCharts({ dashboard }) {

    if (!dashboard) {
        return null;
    }

    const robots = dashboard.robots || [];

    const batteryData = robots.map(robot => ({
        name: robot.id,
        battery: robot.battery
    }));

    const working = robots.filter(r => r.status === "Working").length;
    const idle = robots.filter(r => r.status === "Idle").length;
    const charging = robots.filter(r => r.status === "Charging").length;

    const statusData = [
        { name: "Working", value: working },
        { name: "Idle", value: idle },
        { name: "Charging", value: charging }
    ];

    const COLORS = [
        "#22c55e",
        "#3b82f6",
        "#f59e0b"
    ];

    return (
        <div className="mt-12">

            <h2 className="text-3xl font-bold mb-6">
                📊 Fleet Charts
            </h2>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

                <div className="bg-white rounded-2xl shadow-lg p-6">

                    <h3 className="font-bold text-xl mb-4">
                        Battery Levels
                    </h3>

                    <ResponsiveContainer width="100%" height={300}>

                        <BarChart data={batteryData}>

                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip />
                            <Bar dataKey="battery" />

                        </BarChart>

                    </ResponsiveContainer>

                </div>

                <div className="bg-white rounded-2xl shadow-lg p-6">

                    <h3 className="font-bold text-xl mb-4">
                        Robot Status
                    </h3>

                    <ResponsiveContainer width="100%" height={300}>

                        <PieChart>

                            <Pie
                                data={statusData}
                                dataKey="value"
                                nameKey="name"
                                outerRadius={100}
                                label
                            >

                                {statusData.map((entry, index) => (

                                    <Cell
                                        key={index}
                                        fill={COLORS[index]}
                                    />

                                ))}

                            </Pie>

                            <Tooltip />
                            <Legend />

                        </PieChart>

                    </ResponsiveContainer>

                </div>

            </div>

        </div>
    );
}