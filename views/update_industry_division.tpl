<!DOCTYPE html>
<html>
<head>
    <title>Update Industry and Division</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            flex-direction: column; /* Add this line */
        }

        h2 {
            margin-bottom: 20px; /* Add some margin between h2 and the form */
        }

        form {
            width: 300px; /* Adjust the width as needed */
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>Update Industry and Division</h2>

    <form action="/update" method="post">
        <!-- Add a hidden input field for the industry ID -->
        <input type="hidden" name="id" value="{{str(item['IndustryID'])}}"/>

        <label for="division_name">Division Name:</label>
        <input type="text" name="division_name" value="{{item['DivisionName']}}" required/>

        <label for="company">Company:</label>
        <input type="text" name="company" value="{{item['Company']}}" required/>

        <label for="headquarter">Headquarter:</label>
        <input type="text" name="headquarter" value="{{item['Headquarter']}}" required/>

        <button type="submit">Update</button>
    </form>
</body>
</html>
