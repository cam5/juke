module.exports = {
  "extends": [
    "airbnb",
    "plugin:jsx-a11y/recommended",
  ],
  "env": {
    "browser": true,
    "node": true
  },
  "rules": {
    "jsx-a11y/label-has-associated-control": [
      2,
      {
        "assert": "htmlFor",
        "depth": 3,
      }
    ],
  },
  "plugins": [
    "jsx-a11y"
  ]
};
