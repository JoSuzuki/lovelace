import styled from 'styled-components';

export const WinOverlay = styled.div`
  position: absolute;
  height: 354px;
  width: 354px;
  top: 0px;
  background-color: black;
  opacity: 0.3;
`;

export const WinBox = styled.div`
  position: absolute;
  width: 192px;
  top: 85px;
  left: 80px;
  height: 160px;
  text-align: center;
  align-items: center;
  justify-content: space-around;
  border-radius: 30px;
  border-width: 4px;
  border-color: #400a05;
  border-style: solid;
  background-color: #ffde98;
  opacity: 1;
`

export const WinTitle = styled.h2`
  color: black;
`;

export const Button = styled.button`
  background-color: white;
  margin-top: 10px;
  width: 140px;
  height: 50px;
  font-size: larger;
  display: inline-block;
  cursor: pointer;
  color: #FFFFFF;
  border-radius: 25px;
  border: solid 0px;
  transition-duration: 0.4s;
  background: linear-gradient(180deg, #734223 5%, #400a05 100%);
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
  :hover {
    box-shadow: 0 6px 20px 0 rgba(0,0,0,0.2), 0 0px 0px 0 rgba(0,0,0,0.19);;
  }
  :active {
      position: relative;
      top: 1px;
  }
`;
