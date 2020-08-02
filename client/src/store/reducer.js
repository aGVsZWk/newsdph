import * as actionTypes from './actionTypes'

const defaultState = {
  inputValue: 'Write Something',
  list:[]
}

export default (state=defaultState, action)=>{
  // reducer 里只能接收 state, 不能改变 state
  if (action.type === actionTypes.CHANGE_INPUT){
    let newState = JSON.parse(JSON.stringify(state))
    newState.inputValue = action.value
    return newState;
  }
  if (action.type === actionTypes.ADD_ITEM){
    let newState = JSON.parse(JSON.stringify(state))
    newState.list.push(newState.inputValue)
    newState.inputValue = ''
    return newState;
  }
  if (action.type === actionTypes.DELETE_ITEM){
    let newState = JSON.parse(JSON.stringify(state))
    newState.list.splice(action.index, 1)
    return newState;
  }
  if (action.type === actionTypes.GET_LIST){
    let newState = JSON.parse(JSON.stringify(state))
    console.log(action.data);
    newState.list = action.data.map((item)=>(item.label))
    return newState;
  }
  return state;
}
