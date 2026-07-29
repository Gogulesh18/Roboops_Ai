export default function BatteryBar({ battery }) {

    let color = "bg-green-500";

    if (battery < 70)
        color = "bg-yellow-500";

    if (battery < 30)
        color = "bg-red-500";

    return (

        <div>

            <div className="flex justify-between mb-1">

                <span>Battery</span>

                <span>{battery}%</span>

            </div>

            <div className="w-full bg-gray-300 rounded-full h-3">

                <div
                    className={`${color} h-3 rounded-full transition-all duration-500`}
                    style={{
                        width: `${battery}%`
                    }}
                />

            </div>

        </div>

    );

}