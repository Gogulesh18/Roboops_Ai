export default function Footer() {

    return (

        <footer className="mt-16 bg-slate-900 text-white rounded-t-3xl">

            <div className="max-w-7xl mx-auto px-8 py-8 flex justify-between items-center">

                <div>

                    <h2 className="text-xl font-bold">

                        🤖 RoboOps AI

                    </h2>

                    <p className="text-gray-400">

                        AI Powered Fleet Management Platform

                    </p>

                </div>

                <div className="text-right">

                    <p>

                        Version 1.0

                    </p>

                    <p className="text-gray-400">

                        FastAPI • React • WebSocket

                    </p>

                </div>

            </div>

        </footer>

    );

}