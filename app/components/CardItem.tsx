import * as React from "react";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/app/components/ui/card";
import { StartupType } from "../types";
import Link from "next/link";
import { cn } from "@/lib/utils";
import Image from "next/image";

export function CardItem({ startup }: { startup: StartupType }) {
    const {
        name,
        description,
        image,
        website,
        yc_batch,
        status,
        industries,
        location,
        founded,
        team_size
    } = startup;

    return (
        <Link href={website} target="_blank">
            <Card className="w-full h-96 flex flex-col justify-between">
                <CardHeader className="flex-shrink-0">
                    <div className="flex items-center justify-between">
                        <div className="flex gap-2 justify-start items-center">
                            <div className="w-12 h-12 rounded-full border border-gray-200 shadow-sm overflow-hidden relative">
                                <Image
                                    src={image}
                                    alt={`${name} logo`}
                                    fill
                                    className="rounded-full object-cover"
                                    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                                />
                            </div>
                            <CardTitle className="text-xl font-semibold">{name}</CardTitle>
                        </div>
                        <div className="py-1 px-2 backdrop-blur-md bg-white/10 rounded-lg">
                            <p>{founded}</p>
                        </div>
                    </div>
                    <CardDescription className="text-sm text-gray-600">{description}</CardDescription>
                </CardHeader>
                <CardContent className="flex-1 overflow-y-auto">
                    <div className="grid w-full items-center gap-4">
                        <div className="flex flex-col space-y-2">
                            {industries && industries.length > 0 &&
                                <>
                                    <p><strong>Industries</strong></p>
                                    <div className="flex flex-wrap gap-2">
                                        {industries.map(i =>
                                            <div key={i} className="py-1 px-2 backdrop-blur-md bg-white/10 rounded-lg text-xs">
                                                <p>{i}</p>
                                            </div>
                                        )}
                                    </div>
                                </>
                            }
                            {location && <p><strong>Location:</strong> {location}</p>}
                            <p><strong>Team Size:</strong> {team_size}</p>
                        </div>
                    </div>
                </CardContent>
                <CardFooter className="flex justify-center gap-2">
                    <div className="py-1 px-2 backdrop-blur-md bg-white/10 rounded-lg">
                        <p className="text-sm">YC {yc_batch}</p>
                    </div>
                    <div className={cn("py-1 px-2 rounded-lg bg-opacity-50", status == "Active" ? 'bg-green-300' : 'bg-red-300')}>
                        <p className="text-sm">{status}</p>
                    </div>
                </CardFooter>
            </Card>
        </Link>
    );
}
