import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import KPICards from "../components/KPICards";
import RobotCard from "../components/RobotCard";
import WarehouseMap from "../components/WarehouseMap";
import MissionQueue from "../components/MissionQueue";
import AnalyticsCards from "../components/AnalyticsCards";
import FleetCharts from "../components/FleetCharts";
import AIRecommendation from "../components/AIRecommendation";
import NotificationPanel from "../components/NotificationPanel";
import RecentEvents from "../components/RecentEvents";
import RobotDetails from "../components/RobotDetails";
import Footer from "../components/Footer";

export default function Dashboard() {
    const [dashboard, setDashboard] = useState(null);
    const [connected, setConnected] = useState(false);
    const [selectedRobot, setSelectedRobot] = useState(null);

    useEffect(() => {
        const socket = new WebSocket("ws://127.0.0.1:8000/ws/fleet");

        socket.onopen = () => {
            console.log("✅ Connected");
            setConnected(true);
        };

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setDashboard(data);
        };

        socket.onerror = () => {
            setConnected(false);
        };

        socket.onclose = () => {
            setConnected(false);
        };

        return () => socket.close();
    }, []);

    if (!dashboard) {
        return (
            <div className="min-h-screen bg-slate-900 flex items-center justify-center">
                <h1 className="text-white text-3xl font-bold animate-pulse">
                    🚀 Connecting to RoboOps AI...
                </h1>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-slate-100">

            <Navbar />

            <main className="max-w-7xl mx-auto px-8 py-6">

                {/* Header */}

                <div className="flex items-center justify-between mb-8">

                    <div>

                        <h1 className="text-4xl font-bold text-slate-800">
                            RoboOps AI Dashboard
                        </h1>

                        <p className="text-gray-500 mt-1">
                            Live Warehouse Fleet Monitoring
                        </p>

                    </div>

                    <span
                        className={`px-5 py-2 rounded-full text-white font-semibold shadow-lg ${
                            connected
                                ? "bg-green-600"
                                : "bg-red-600"
                        }`}
                    >
                        {connected ? "🟢 LIVE" : "🔴 OFFLINE"}
                    </span>

                </div>

                {/* KPI */}

                <KPICards dashboard={dashboard} />

                {/* Robot Fleet */}

                <section className="mt-12">

                    <h2 className="text-3xl font-bold mb-6">
                        🤖 Robot Fleet
                    </h2>

                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                        {dashboard.robots?.map((robot) => (

                            <RobotCard
                                key={robot.id}
                                robot={robot}
                                onClick={() => setSelectedRobot(robot)}
                            />

                        ))}

                    </div>

                </section>

                {/* Warehouse */}

                <section className="mt-14">

                    <WarehouseMap robots={dashboard.robots} />

                </section>

                {/* Mission Queue */}

                <section className="mt-14">

                    <MissionQueue robots={dashboard.robots} />

                </section>

                {/* Analytics */}

                <section className="mt-14">

                    <AnalyticsCards dashboard={dashboard} />

                </section>

                {/* Charts */}

                <section className="mt-14">

                    <FleetCharts dashboard={dashboard} />

                </section>

                {/* AI Recommendation */}

                <section className="mt-14">

                    <AIRecommendation dashboard={dashboard} />

                </section>

                {/* Notifications */}

                <section className="mt-14">

                    <NotificationPanel robots={dashboard.robots} />

                </section>

                {/* Recent Events */}

                <section className="mt-14">

                    <RecentEvents
                        events={dashboard.recent_events || []}
                    />

                </section>

            </main>

            {/* Robot Details Drawer */}

            <RobotDetails
                robot={selectedRobot}
                onClose={() => setSelectedRobot(null)}
            />

            {/* Footer */}

            <Footer />

        </div>
    );
}