import StatusBadge from "./StatusBadge";

export default function MissionQueue({ robots = [] }) {

    const pending = robots.filter(
        robot => robot.status === "Idle"
    );

    const running = robots.filter(
        robot => robot.status === "Working"
    );

    const charging = robots.filter(
        robot => robot.status === "Charging"
    );

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-2xl font-bold mb-6">
                📋 Mission Queue
            </h2>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                {/* Pending */}

                <div>

                    <h3 className="text-lg font-bold text-blue-600 mb-4">

                        ⏳ Pending

                    </h3>

                    <div className="space-y-3">

                        {pending.length === 0 ? (

                            <p className="text-gray-400">
                                No Pending Missions
                            </p>

                        ) : (

                            pending.map(robot => (

                                <div
                                    key={robot.id}
                                    className="border rounded-xl p-4 bg-slate-50"
                                >

                                    <p className="font-bold">

                                        🤖 {robot.id}

                                    </p>

                                    <p className="text-gray-600">

                                        Waiting for Task

                                    </p>

                                    <div className="mt-3">

                                        <StatusBadge status={robot.status} />

                                    </div>

                                </div>

                            ))

                        )}

                    </div>

                </div>

                {/* Running */}

                <div>

                    <h3 className="text-lg font-bold text-green-600 mb-4">

                        🚚 Running

                    </h3>

                    <div className="space-y-3">

                        {running.length === 0 ? (

                            <p className="text-gray-400">

                                No Running Missions

                            </p>

                        ) : (

                            running.map(robot => (

                                <div
                                    key={robot.id}
                                    className="border rounded-xl p-4 bg-slate-50"
                                >

                                    <p className="font-bold">

                                        🤖 {robot.id}

                                    </p>

                                    <p className="text-gray-600">

                                        {robot.task}

                                    </p>

                                    <p className="text-sm text-gray-500 mt-1">

                                        ➜ {robot.destination}

                                    </p>

                                    <div className="mt-3">

                                        <StatusBadge status={robot.status} />

                                    </div>

                                </div>

                            ))

                        )}

                    </div>

                </div>

                {/* Charging */}

                <div>

                    <h3 className="text-lg font-bold text-yellow-600 mb-4">

                        ⚡ Charging

                    </h3>

                    <div className="space-y-3">

                        {charging.length === 0 ? (

                            <p className="text-gray-400">

                                No Robots Charging

                            </p>

                        ) : (

                            charging.map(robot => (

                                <div
                                    key={robot.id}
                                    className="border rounded-xl p-4 bg-slate-50"
                                >

                                    <p className="font-bold">

                                        🤖 {robot.id}

                                    </p>

                                    <p className="text-gray-600">

                                        Battery : {robot.battery}%

                                    </p>

                                    <div className="mt-3">

                                        <StatusBadge status={robot.status} />

                                    </div>

                                </div>

                            ))

                        )}

                    </div>

                </div>

            </div>

        </div>

    );

}