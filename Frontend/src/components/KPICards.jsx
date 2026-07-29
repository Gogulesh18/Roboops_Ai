export default function KPICards({ dashboard }) {
  const cards = [
    {
      title: "Total Robots",
      value: dashboard.total_robots,
      color: "bg-blue-600",
      icon: "🤖",
    },
    {
      title: "Working",
      value: dashboard.working,
      color: "bg-green-600",
      icon: "🟢",
    },
    {
      title: "Charging",
      value: dashboard.charging,
      color: "bg-yellow-500",
      icon: "⚡",
    },
    {
      title: "Fleet Health",
      value: `${dashboard.fleet_health_score}%`,
      color: "bg-purple-600",
      icon: "❤️",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {cards.map((card) => (
        <div
          key={card.title}
          className={`${card.color} rounded-2xl shadow-lg p-6 text-white`}
        >
          <div className="flex justify-between items-center">
            <div>
              <p className="text-sm opacity-80">{card.title}</p>

              <h2 className="text-4xl font-bold mt-2">
                {card.value}
              </h2>
            </div>

            <div className="text-4xl">
              {card.icon}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}