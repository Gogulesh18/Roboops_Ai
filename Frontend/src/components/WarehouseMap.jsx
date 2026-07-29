import WarehouseCell from "./WarehouseCell";

export default function WarehouseMap({ robots = [] }) {

    const warehouse = [
        ["A1", "A2", "A3", "A4", "A5", "A6"],
        ["B1", "B2", "B3", "B4", "B5", "B6"],
        ["C1", "C2", "C3", "C4", "C5", "C6"],
        ["D1", "D2", "D3", "D4", "D5", "D6"],
        ["E1", "E2", "E3", "E4", "E5", "E6"],
    ];

    const getRobot = (cell) =>
        robots.find((robot) => robot.location === cell);

    const getCellType = (cell) => {

        if (cell === "A6")
            return "charging";

        if (cell === "E1")
            return "pickup";

        if (cell === "E6")
            return "dispatch";

        if (
            cell.startsWith("B") ||
            cell.startsWith("D")
        )
            return "rack";

        return "path";

    };

    return (

        <div className="bg-white rounded-3xl shadow-xl p-8">

            <div className="flex justify-between items-center mb-8">

                <div>

                    <h2 className="text-3xl font-bold">

                        🏭 Warehouse Digital Twin

                    </h2>

                    <p className="text-gray-500 mt-2">

                        Live Robot Positions

                    </p>

                </div>

                <div className="flex gap-6 text-sm">

                    <Legend color="bg-slate-700" text="Rack" />
                    <Legend color="bg-green-300" text="Charging" />
                    <Legend color="bg-blue-300" text="Pickup" />
                    <Legend color="bg-orange-300" text="Dispatch" />
                    <Legend color="bg-slate-100" text="Path" />

                </div>

            </div>

            <div className="space-y-3">

                {

                    warehouse.map((row, rowIndex) => (

                        <div
                            key={rowIndex}
                            className="flex gap-3 justify-center"
                        >

                            {

                                row.map((cell) => (

                                    <WarehouseCell
                                        key={cell}
                                        label={cell}
                                        type={getCellType(cell)}
                                        robot={getRobot(cell)}
                                    />

                                ))

                            }

                        </div>

                    ))

                }

            </div>

            <div className="mt-8 grid md:grid-cols-4 gap-5">

                <StatCard
                    title="Robots Online"
                    value={robots.length}
                    icon="🤖"
                    color="bg-blue-100"
                />

                <StatCard
                    title="Charging"
                    value={
                        robots.filter(
                            r => r.status === "Charging"
                        ).length
                    }
                    icon="⚡"
                    color="bg-green-100"
                />

                <StatCard
                    title="Working"
                    value={
                        robots.filter(
                            r => r.status === "Working"
                        ).length
                    }
                    icon="📦"
                    color="bg-yellow-100"
                />

                <StatCard
                    title="Idle"
                    value={
                        robots.filter(
                            r => r.status === "Idle"
                        ).length
                    }
                    icon="🛑"
                    color="bg-red-100"
                />

            </div>

        </div>

    );

}

function Legend({ color, text }) {

    return (

        <div className="flex items-center gap-2">

            <div className={`w-4 h-4 rounded ${color}`} />

            <span>{text}</span>

        </div>

    );

}

function StatCard({

    title,

    value,

    icon,

    color

}) {

    return (

        <div className={`${color} rounded-2xl p-5`}>

            <div className="text-3xl">

                {icon}

            </div>

            <div className="mt-3 text-gray-600">

                {title}

            </div>

            <div className="text-3xl font-bold">

                {value}

            </div>

        </div>

    );

}