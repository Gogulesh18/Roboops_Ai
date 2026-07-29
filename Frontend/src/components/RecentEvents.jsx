export default function RecentEvents({ events = [] }) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6 mt-12">

            <div className="flex items-center justify-between mb-6">

                <h2 className="text-2xl font-bold">
                    🕒 Recent Events
                </h2>

                <span className="text-sm text-gray-500">
                    Live Activity
                </span>

            </div>

            {events.length === 0 ? (

                <div className="text-center py-8 text-gray-400">

                    No recent events

                </div>

            ) : (

                <div className="space-y-4">

                    {events.map((event, index) => (

                        <div
                            key={index}
                            className="flex items-start gap-4 border-b pb-4 last:border-none"
                        >

                            <div className="text-2xl">

                                {event.icon || "🤖"}

                            </div>

                            <div className="flex-1">

                                <p className="font-semibold">

                                    {event.message}

                                </p>

                                <p className="text-sm text-gray-500">

                                    {event.time}

                                </p>

                            </div>

                        </div>

                    ))}

                </div>

            )}

        </div>

    );

}