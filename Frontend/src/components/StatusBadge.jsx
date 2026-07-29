export default function StatusBadge({ status }) {

    const statusConfig = {
        Working: {
            color: "bg-green-100 text-green-700",
            icon: "🟢"
        },
        Idle: {
            color: "bg-blue-100 text-blue-700",
            icon: "🔵"
        },
        Charging: {
            color: "bg-yellow-100 text-yellow-700",
            icon: "🟡"
        },
        Error: {
            color: "bg-red-100 text-red-700",
            icon: "🔴"
        },
        Maintenance: {
            color: "bg-orange-100 text-orange-700",
            icon: "🟠"
        }
    };

    const current =
        statusConfig[status] || {
            color: "bg-gray-100 text-gray-700",
            icon: "⚪"
        };

    return (

        <span
            className={`
                inline-flex
                items-center
                gap-2
                px-3
                py-1
                rounded-full
                text-sm
                font-semibold
                ${current.color}
            `}
        >

            <span>{current.icon}</span>

            {status}

        </span>

    );

}