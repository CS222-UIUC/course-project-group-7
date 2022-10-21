import React from 'react'
import { makeStyles } from '@material-ui/core/styles'

//const Grid = () => <div data-testid="Grid">Grid Component</div>

const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
  },
  item: {
    border: '1px solid blue',
    flexBasis: '33%',
    maxWidth: '33%',
  },
  itemFlexGrow: {
    flexGrow: 1,
    border: '1px solid red',
  },
}))

export default function Grid() {
  const classes = useStyles()

  return (
    <div className={classes.root}>
      <h3> Student Directory </h3>
      <div className={classes.container}>
        <div className={classes.item}> Name</div>
        <div className={classes.item}> Email </div>
        <div className={classes.item}> Classes </div>
        <div className={classes.item}> Hobbies </div>
      </div>
    </div>
  )
}
