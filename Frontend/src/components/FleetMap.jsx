export default function FleetMap({ robots }) {

    const cells = [
        "A1", "A2", "A3",
        "B1", "B2", "B3",
        "C1", "C2", "C3"
    ];

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-10">

            <h2 className="text-2xl font-bold mb-6">

                🏭 Warehouse Fleet Map

            </h2>

            <div className="grid grid-cols-3 gap-4">

                {cells.map(cell => {

                    const robot = robots.find(
                        r => r.location === cell
                    );

                    return (

                        <div
                            key={cell}
                            className="border rounded-xl h-28 flex flex-col items-center justify-center bg-slate-50"
                        >

                            <span className="text-gray-500 text-sm">

                                {cell}

                            </span>

                            {

                                robot ? (

                                    <>

                                        <div className="text-3xl">

                                            🤖

                                        </div>

                                        <p className="font-bold">

                                            {robot.id}

                                        </p>

                                        <p className="text-xs">

                                            {robot.status}

                                        </p>

                                    </>

                                ) : (

                                    <div className="text-gray-300 text-3xl">

                                        □

                                    </div>

                                )

                            }

                        </div>

                    );

                })}

            </div>

        </div>

    );

}