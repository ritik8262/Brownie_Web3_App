import React, { useEffect, useState } from "react";
import { useEthers } from "@usedapp/core"
import helperConfig from "../helper-config.json"
import { Button, Input, makeStyles, CircularProgress } from "@material-ui/core";



const useStyles = makeStyles((theme) => ({
    title: {
        color: theme.palette.common.black,
        textAlign: "center",
        padding: theme.spacing(4)
    }
}))

export const Main = () => {
    const { chainId, error } = useEthers()
    const networkName = chainId ? helperConfig[chainId] : "dev"

    const classes = useStyles()

    const { account } = useEthers()

    const [amount, setAmount] = useState<number | string | Array<number | string>>(0)

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const newAmount = event.target.value === "" ? "" : Number(event.target.value)
        setAmount(newAmount)
        console.log(newAmount)
    }




    return (
        <>
            <h2 className={classes.title}>
                Hey I'm Ritik
            </h2>
            <div>
                Wave at me on the Ethereum blockchain! Maybe send a sweet message too?
                Connect your wallet, write your message, and then wave.
                <Input
                    onChange={handleInputChange} />
                <Button
                    color="primary"
                    size="large">
                    Wave!!
                </Button>
            </div>
        </>
    )

}