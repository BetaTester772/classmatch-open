import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import axios from "axios"
export function Resister() {
    const client = axios.create()
    const navigate = useNavigate()
    const [userInfo, setUserInfo] = useState({
      'id' : '',
      'pw' : ''
    })
    const [msg, setMsg] = useState('')
    const [btnTxt, setBtnTxt] = useState('내 시간표 등록하기')
    const onClick = () => {
        setBtnTxt('로딩중...')
        client.post('http://localhost:8000/resister', userInfo)
        .then(res=>{
          setBtnTxt('내 시간표 등록하기')
          if (res.data === 'success') {
            navigate('/browse')
          } else {
            setMsg(res.data)
          }
        })
        .catch(err=>{
          setMsg("예기치 못한 에러 발생")
          setBtnTxt('내 시간표 등록하기')
        })
      }
    const onChange = (e) => {
        setUserInfo({
          ...userInfo,
          [e.target.name] : e.target.value
        })
      }
    return(
        <div id="contain">
            <h3>내 시간표 등록하기</h3>
            <input placeholder="인트라넷 아이디" id="in" onChange={onChange} name="id"/>
            <input placeholder="인트라넷 비밀번호" id="in" onChange={onChange} name="pw"/>
            <button variant="primary" type="submit" onClick={onClick} id='btn'>
              {btnTxt}
            </button>
            <br/>
            <label id='err'>{msg}</label>
        </div>
    )
}