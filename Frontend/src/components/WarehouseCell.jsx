export default function WarehouseCell({
    label,
    type = "empty",
    robot = null,
}) {

    const base =
        "w-16 h-16 rounded-xl border flex items-center justify-center text-xs font-bold transition-all duration-300";

    const styles = {
        rack: "bg-slate-700 border-slate-800 text-white",
        charging: "bg-green-200 border-green-500",
        pickup: "bg-blue-200 border-blue-500",
        dispatch: "bg-orange-200 border-orange-500",
        path: "bg-slate-100 border-slate-300",
        empty: "bg-white border-slate-300",
    };

    return (

        <div className={`${base} ${styles[type]}`}>

            {robot ? (

                <div className="flex flex-col items-center">

                    <span className="text-2xl animate-bounce">

                        🤖

                    </span>

                    <span className="text-[10px]">

                        {robot.id}

                    </span>

                </div>

            ) : (

                <span>

                    {label}

                </span>

            )}

        </div>

    );

}