import StatusBadge from "./StatusBadge";
import BatteryBar from "./BatteryBar";

export default function RobotDetails({ robot, onClose }) {

    if (!robot) return null;

    return (

        <div className="fixed inset-0 bg-black/40 flex justify-end z-50">

            <div className="w-[420px] bg-white h-screen shadow-2xl p-6 overflow-y-auto">

                <div className="flex justify-between items-center mb-6">

                    <h2 className="text-2xl font-bold">

                        🤖 {robot.id}

                    </h2>

                    <button
                        onClick={onClose}
                        className="text-2xl font-bold hover:text-red-500"
                    >
                        ✕
                    </button>

                </div>

                <div className="space-y-5">

                    <div>

                        <p className="font-semibold mb-2">
                            Status
                        </p>

                        <StatusBadge status={robot.status} />

                    </div>

                    <div>

                        <p className="font-semibold mb-2">
                            Battery
                        </p>

                        <BatteryBar battery={robot.battery} />

                    </div>

                    <div className="grid grid-cols-2 gap-4">

                        <Info title="Location" value={robot.location} />

                        <Info title="Destination" value={robot.destination} />

                        <Info title="Task" value={robot.task} />

                        <Info title="Speed" value={`${robot.speed} m/s`} />

                        <Info
                            title="Temperature"
                            value={`${robot.temperature} °C`}
                        />

                        <Info
                            title="Progress"
                            value={`${robot.task_progress}%`}
                        />

                    </div>

                    <div>

                        <p className="font-semibold mb-2">

                            Route

                        </p>

                        <div className="bg-slate-100 rounded-xl p-3">

                            {

                                robot.route?.length

                                    ? robot.route.join(" ➜ ")

                                    : "No Route"

                            }

                        </div>

                    </div>

                </div>

            </div>

        </div>

    );

}

function Info({ title, value }) {

    return (

        <div className="bg-slate-100 rounded-xl p-3">

            <p className="text-gray-500 text-sm">

                {title}

            </p>

            <h3 className="font-bold mt-1">

                {value}

            </h3>

        </div>

    );

}