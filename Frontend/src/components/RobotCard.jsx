import BatteryBar from "./BatteryBar";
import StatusBadge from "./StatusBadge";

export default function RobotCard({ robot, onClick }) {
    return (
        <div
            onClick={onClick}
            className="bg-white rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-300 cursor-pointer hover:-translate-y-2 border border-slate-200 overflow-hidden"
        >
            {/* Header */}

            <div className="bg-gradient-to-r from-indigo-600 to-blue-600 text-white p-5">

                <div className="flex justify-between items-center">

                    <div>

                        <h2 className="text-2xl font-bold">

                            🤖 {robot.id}

                        </h2>

                        <p className="text-blue-100 text-sm mt-1">

                            Autonomous Mobile Robot

                        </p>

                    </div>

                    <StatusBadge status={robot.status} />

                </div>

            </div>

            {/* Body */}

            <div className="p-5 space-y-5">

                {/* Battery */}

                <div>

                    <div className="flex justify-between mb-2">

                        <span className="font-semibold">

                            Battery

                        </span>

                        <span className="font-bold">

                            {robot.battery}%

                        </span>

                    </div>

                    <BatteryBar battery={robot.battery} />

                </div>

                {/* Robot Info */}

                <div className="grid grid-cols-2 gap-4">

                    <Info
                        title="📍 Location"
                        value={robot.location}
                    />

                    <Info
                        title="🎯 Destination"
                        value={robot.destination}
                    />

                    <Info
                        title="📦 Task"
                        value={robot.task}
                    />

                    <Info
                        title="⚡ Speed"
                        value={`${robot.speed} m/s`}
                    />

                    <Info
                        title="🌡 Temperature"
                        value={`${robot.temperature}°C`}
                    />

                    <Info
                        title="📈 Progress"
                        value={`${robot.task_progress ?? 0}%`}
                    />

                </div>

                {/* Route */}

                <div>

                    <p className="font-semibold mb-2">

                        Route

                    </p>

                    <div className="bg-slate-100 rounded-xl p-3 text-sm">

                        {robot.route?.length
                            ? robot.route.join(" ➜ ")
                            : "No Active Route"}

                    </div>

                </div>

                {/* Footer */}

                <div className="flex justify-between items-center border-t pt-4">

                    <span className="text-sm text-gray-500">

                        Click for details

                    </span>

                    <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-xl">

                        View

                    </button>

                </div>

            </div>
        </div>
    );
}

function Info({ title, value }) {
    return (
        <div className="bg-slate-50 rounded-xl p-3">

            <p className="text-xs text-gray-500">

                {title}

            </p>

            <h3 className="font-semibold mt-1">

                {value}

            </h3>

        </div>
    );
}